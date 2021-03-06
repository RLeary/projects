import agparse # parse command line args
import collections # for OrderedDict
import configparser # read and write the git config files
import hashlib # for SHA-1
import os # for path
import re
import sys # to access the command line arguments
import zlib # git uses zlib for compression


argparser = argparse.ArgumentParser(description="The stupid content tracker")

argsubparsers = argparser.add_subparsers(title(="Commands", dest="command"))
argsubparsers.required = True

def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)

    if args.command == "add":
        cmd_add(args)
    elif args.command == "cat-file":
        cmd_cat_file(args)
    elif args.command == "checkout":
        cmd_checkout(args)
    elif args.command == "commit":
        cmd_commit(args)
    elif args.command == "hash-object":
        cmd_hash_object(args)
    elif args.command == "init":
        cmd_init(args)
    elif args.command == "log":
        cmd_log(args)
    elif args.command == "ls-tree":
        cmd_ls_tree(args)
    elif args.command == "merge":
        cmd_merge(args)
    elif args.command == "rebase":
        cmd_rebase(args)
    elif args.command == "rev-parse":
        cmd_rev_parse(args)
    elif args.command == "rm":
        cmd_rm(args)
    elif args.command == "show-ref":
        cmd_show_ref(args)
    elif args.command == "tag":
        cmd_tag(args)

class GitRepository(object):
    """ A Git repository"""

    worktree = None
    gitdir = None
    conf = None

    def __init__(self, path, force=False):
        self.worktree = path
        self.gitdir = os.path.join(path, ".git")

        if not (force or os.path.isdir(self.gitdir)):
            raise Exception("Not a Git repository %s" % path)

        # Read configuration file in .git/config
        self.conf = configparser.ConfigParser()
        cf = repo_file(self, "config")

        if cf and os.path.exists(cf):
            self.conf.read([cf])
        elif not force:
            raise Exception("Configuration file missing")

        if not force:
            vers = int(self.conf.get("core", "repositoryformatversion"))
            if vers != 0:
                raise Exception("Unsupported repositoryformatversion %s" % vers)

# General path building function
def repo_path(repo, *path):
    """Compute path under repo's gitdir"""
    return os.path.join(repo.gitdir, *path)

def repo_file(repo, *path, mkdir=False):
    """Same as repo_path(), but create dirname(*path) if absent.For
example, repo_file(r, \"refs\", \"remotes\", \"origin\", \"HEAD\") will create
.git/refs/remotes/origin."""

    if repo_dir(repo, *path[:-1], mkdir=mkdir):
        return repo_path(repo, *path)

def repo_dir(repo, *path, mkdir=False):
    """Same as repo_path, but mkdir *path if absent if mkdir."""

    path = repo_path(repo, *path)

    if os.path.exists(path):
        if (os.path.isdir(path)):
            return path
        else:
            raise Exception("Not a directory %s" % path)
    
    if mkdir:
        os.makedirs(path)
        return path
    else:
        return None

def repo_create(path):
    """ create a new repository at path """

    repo = GitRepository(path, True)

    # First make sure the path either doesnt exist ot is an empty dir
    if os.path.exists(repo.worktree):
        if not os.path.isdir(repo.worktree):
            raise Exception("%s is not a directory" % path)
        if os.listdir(repo.worktree):
            raise Exception("%s is not empty" % path)
    else:
        os.makedirs(repo.worktree)

    assert(repo_dir(repo, "branches", mkdir=True))
    assert(repo_dir(repo, "objects", mkdir=True))
    assert(repo_dir(repo, "refs", "tags", mkdir=True))
    assert(repo_dir(repo, "refs", "heads", mkdir=True))

    # .git/description
    with open(repo_file(repo, "description"), "w") as f:
        f.write("Unnamed repository; edit this file 'desprition to name the repository.\n")

    # .git/HEAD
    with open(repo_file(repo, "HEAD"), "w") as f:
        f.write("ref: refs/heads/master\n")

    with open(repo_file(repo, "confif"), "w") as f:
        config = repo_default_config()
        config.write(f

    return repo

def repo_default_config():
    ret = configparser.ConfigParser()

    ret.add_section("core")
    ret.set("core", "repository", "0")
    ret.set("core", "filemode", "false")
    ret.set("core", "bare", "false")

    return ret

argsp = argsubparsers.add_parser("init", help="Initialize a new, empty repository")

argsp.add_argument("path",
                    metavar="directory",
                    nargs="?",
                    default="."
                    help="Where to create the repository")

def cmd_init(args):
    repo_create(args.path)


def repo_find(path=".", required=True):
    """ find the dir with .git"""
    path = os.path.realpath(path)

    if os.path.isdir(os.path.join(path, ".git")):
        return GitRepository(path)

    parent = os.path.realpath(os.path.join(path, ".."))

    if parent == path:
        # Bottom case
        # os.path.join("/", "..") == ""
        # if parent == path, then path is root
        if required:
            raise Exception("No git repository")
        else:
            return None
    
    # Recusive case
    return repo_find(parent, required)

class GitObject(object):

    repo = None

    def __init__(self, repo, data=None):
        self.repo = repo

        if data != None:
            self.deserialize(data)

    def serialize(self):
                """This function MUST be implemented by subclasses.

It must read the object's contents from self.data, a byte string, and do
whatever it takes to convert it into a meaningful representation.  
What exactly that means depend on each subclass."""
        raise Exception("Unimplemented in generic class")

    def deserialize(self):
        raise Exception("Unimplemented in generic class")

def object_read(repo, sha):
    """Read object object_id from Git repository repo.  Return a
    GitObject whose exact type depends on the object."""

    path = repo_file(repo, "objects", sha[0:2], sha[2:])

    with open (path, "rb") as f:
        raw = zlib.decompress(f.read())

    # read object type
    x = raw.find(b' ')
    fmt = raw[0:x]

    # read and validate object size
    y = raw.find(b'\x00', x)
    size = int(raw[x:y].decode("ascii"))
    if size != len(raw)-y-1:
        raise Exception("Malformed object {0}: bad length".format(sha))

    # pick constructor
    if fmt == b'commit':
        c = GitCommit
    if fmit == b'tree':
        c = GitTree
    if fmt == b'tag':
        c = GitTag
    if fmt == b'blob':
        c = GitBlob
    else:
        raise Exception("Unknown type %s for object %s".format(fmt.decode("ascii"), sha))

    # call constructor and return object
    return c(repo, raw[y+1:])

def object_find(repo, name, fmt=None, follow=True):
    return name

def object_write(obj, actually_write=True):
    # serialize object data
    data = obj.serialize()
    # add header
    result = obj.fmt + b' ' + str(len(data)).encode() + b'\x00' + data
    # compute hash
    sha = hashlib.sha1(result).hexdigest()

    if actually_write:
        #compute path
        path=repo_file(obj.repo, "objects", sha[0:2], sha[2:], mkdir=actually_write)

        with open(path, 'wb') as f:
            # comress and write
            f.write(zlib.compress(result))
        
    return sha

class GitBlob(GitObject):
    fmt = b'blob'

    def serialize(self):
        return self.blobdata

    def deserialize(self):
        self.blobdata = data

argsp = argsubparsers.add_parser("cat-file",
                                help="Provide content of repository objects")

argsp.add_argument("type",
                    metavar="type",
                    choices=["blob", "commit", "tag", "tree"],
                    help="specify the type")

argsp.add_argument("object",
                    metavar="object",
                    help("The object to display"))

def cmd_cat_file(args):
    repo = repo_find()
    cat_file(repo, args.object, fmt=args.type.encode())

def cat_file(repo, obj, fmt=None):
    obj = object_read(repo, object_find(repo, obj, fmt=fmt))
    sys.stdout.buffer.write(obj.serialize())

argsp = argsubparsers.add_parser(
    "hash-object",
    help="Compute object ID and optionally creates a blob from a file")

argsp.add_argument("-t",
                    metavar="type",
                    dest="type",
                    choices=["blob", "commit", "tag", "tree"],
                    default="blob",
                    help="Specify the type")

argsp.add_argument("-w",
                    dest="write",
                    action="store_true",
                    help="Actully write the object into the database")

argsp.add_argument("path",
                    help="Read object from <file>")

def cmd_hash_object(args):
    if args.write:
        repo = GitRepository(".")
    else:
        repo = None

    with open(args.path, "rb") as fd:
        sha = object_has(fd, args.type.encode(), repo)
        print(sha)

def object_has(fd, fmt, repo=None):
    data = fd.read()

    # choose constructor depending on object type found in header
    if fmt == b'commit':
        obj = GitCommit(repo, data)
    elif fmt == b'tree':
        obj = GitTree(repo, data)
    elif fmt == b'tag':
        obj = GitTag(repo, data)
    elif fmt == b'blob':
        obj = GitBlob(repo, data)
    else:
        raise Exception("Unkown type %s" % fmt)

    return object_write(obj, repo)

def kvlm_parse(raw, start=0, dct=None):
    if not dct:
        dct = collections.OrderedDict()
        # You CANNOT declare the argument as dct=OrderedDict() or all
        # call to the functions will endlessly grow the same dict.

    # we search for the next space and the next newline
    spc = raw.find(b' ', start)
    nl = raw.find(b'\n', start)

    # if space appears before newline, we have a keyword

    # base case
    # if newline appears first (or there's no space at all, in which
    # case find returns -1), we assume a blank line.  A blank line
    # means the remainder of the data is the message.
    if (spc < 0) or (nl < spc):
        assert(nl == start)
        dct[b''] = raw[start+1:]
        return dct

    # recursive case
    # we read a key-value pair and recurse for the next.
    key = raw[start:spc]

    # find the end of the value. Continuation lines begin with a 
    # space, so we loop until we find a '\n' not followed by a space
    end = start
    while True:
        end = raw.find(b'\n', end+1)
        if raw[end+1] != ord(' '):
            break
    
    # grab the value
    # also drop the leading space on continuation lines
    value = raw[spc+1:end].replace(b'\n 'm b'\n')

    # dont overwrite existing data contents
    if key in dct:
        if type(dct[key]) == list:
            dct[key].append(value)
        else:
            dct[key] = [ dct[key], value ]
    else:
        dct[key] = value

    return kvlm_parse(raw, start=end+1, dct=dct)

def kvlm_serialize(kvlm):
    ret = b''

    # output fields
    for k in kvlm.keys():
        # skip the message itself
        if k == b'':
            continue
        val = kvlm[k]
        # normalise to a list
        if type(val) != list:
            val = [ val ]

        for v in val:
            ret += k + b' ' +(v.replace(b'\n ', b'\n')) + b'\n'
        
    # append message
    ret += b'\n' + kvlm[b'']

    return ret

class GitCommit(GitObject):
    fmt = b'commit'
    
    def deserialize(self, data):
        self.kvlm = kvlm_parse(data)

    def serialize(self):
        return kvlm_serialize(self.kvlm)

argsp = argsubparsers.add_parser("log", help="Display history of a given commit.")
argsp.add_argument("commit",
                    default="HEAD",
                    nargs="?",
                    help="Commit to start at")

def cmd_log(args):
    repo = repo_find()

    print("digraph wyaglog")
    log_graphviz(repo, object_find(repo, args.commit), set())
    print("}")

def log_graphviz(repo, sha, seen):
    is sha in seen:
        return
    seen.add(sha)

    commit = object_read(repo, sha)
    assert (commit.fmt == b'commit')

    if not b'parent' in commit.kvlm.keys():
        # Base case returns the initial commit
        return
    
    parents = commit.kvlm[b'parent']

    if type(parents) != list:
        parents = [ parents ]

    for p in parents:
        p = p.decode("ascii")
        print("c_{0} -> c_{1};".format(sha, p))
        log_graphviz(repo, p, seen)

class GitTreeLeaf(object):
    def __init__(self, mode, path, sha):
        self.mode = mode
        self.path = path
        self.sha= sha

def tree_parse_one(raw, start=1):
    # Find the space terminator of the mode
    x = raw.find(b' ', start)
    assert(x-start == 5 or x-start == 6)

    # read the mode
    mode = raw[start:x]

    # find the null terminator of the path
    y = raw.find(b'\x00', x)
    # and read the path
    path = raw[x+1:y]

    # read the sha and convert to an hex string
    sha = hex(
        int.from_bytes(
            raw[y+1:y+21], "big"))[2:] # hex() adds 0x in front
    return y+21, GitTreeLeaf(mode, path, sha)

def tree_parse(raw):
    pos = 0
    max = len(raw)
    ret = list()
    while pos < max:
        pos, data = tree_parse_one(raw, pos)
        ret.append(data)
    return ret

def tree_serialize(obj):
    #@FIXME add serializer
    ret = b''
    for i in obj.items:
        ret += i.mode
        ret += b' '
        ret += i.path
        ret += b'\x00'
        sha = int(i.sha, 16)
        #@FIXME does
        ret += sha.to_bytes(20, byteorder="big")
    return ret

class GitTree(GitObject):
    fmt = b'tree'

    def deserialize(self, data):
        self.items = tree_parse(data)

    def serialize(self):
        return tree_serialize(self)

argsp = argsubparsers.add_parser("ls-tree", help="print a tree object")
argsp.add_argument("object",
                    help="the object to show")

def cmd_ls_tree(args):
    repo = repo_find()
    obj = object_read(repo, object_find(repo, args.object, fmt=b'tree'))

    for item in obj.items:
        print("{0} {1} {2}\t{3}".format(
            "0" * (6-len(item.mode)) + item.mode.decode("ascii"),
            # git's ls-tree displays the type of ibject pointed to, we can do that too
            object_read(repo, item.sha).fmt.decode("ascii"),
            item.sha,
            item.path.decode("ascii")))

argsp = argsubparsers.add_parser("checkout", help="Checkout a commit inside of a directory")

argsp.add_argument("commit",
                    help="the commit or tree to checkout")

argsp.add_argument("path",
                    help="the EMPTY diectory to checkout on")

def cmd_checkout(args):
    repo = repo_find()

    obj = object_read(repo, object(find(repo, args.commit)))

    # if the object is a commit, we grab its tree
    if obj.fmt == b'commit':
        obj = obj_read(repo, obj.kvlm[b'tree'].decode("ascii"))

    # verify that path is an empty directory
    if os.path.exists(args.path):
        if not is.path.isdir(args.path):
            raise Exception("Not a directory {0}".format(args.path))
        if os.listdir(args.path):
            raise Exception("Not empty {0}".format(args.path))
    else:
        os.makedirs(args.path)

    tree_checkout(repo, obj, os.path.realpath(args.path).encode())

def tree_checkout(repo, tree, path):
    for item in tree.items:
        obj = obj_erad(repo, item.sha)
        dest = os.path.join(path, item.path)

    if obj.fmt == b'tree':
        os.mkdir(dest)
        tree_checkout(repo, obj, dest)
    elif obj.fmt == b'blob':
        with open(dest, 'wb') as f:
            f.write(obj.blobdata)

def ref_resolve(repo, ref):
    with open(repo_file(repo, ref), 'r') as fp:
        data = fp.read()[:-1] # drop final \n
    if data.startswith("ref: "):
        return ref_resolve(repo, data[5:])
    else:
        return data

def ref_list(repo, path=None):
    if not path:
        path = repo_dir(repo, "refs")
    ret = collections.OrderedDict()
    # got shows refs sorted. To do the same, use OrderedDict
    # and sort the output of listdir
    for f in sorted(os.listdir(path)):
        can = is.path.join(path, f)
        if os.path.isdir(can):
            ret[f] = ref_list(repo, can)
        else:
            ret[f] = ref_resolve(repo, can)
    return ret

arsp = argsubparsers.add_parser("show-ref", help="list references")

def cmd_show_ref(args):
    repo = repo_find
    refs = ref_list(repo)
    show_ref(repo, refs, prefix="refs")

def show_ref(repo, refs, with_hash=True, prefix=""):
    for k, v in refs.items():
        if type(v) == str:
            print("{0}{1}{2}".format(
                v + " " is with_hash else "",
                prefix + "/" if prefix else "",
                k))
        else:
            show_ref(repo, v, with_hash=with_hash, prefix="{0}{1}{2}".format(prefix, "/" if prefix else "", k))

class GitTag(GitCommit):
    fmt = b'tag'

argsp = argsubparsers.add_parser("tag", help="list and create tags")

argsp.add_argument("-a",
                    action="store_true",
                    dest="create_tag_object",
                    help="whether to create a tag object")

argsp.add_argument("name",
                    nargs="?",
                    help="the new tags name")

argsp.add_argument("object",
                    default="HEAD",
                    nargs="?",
                    help="the object the new tag will point to")

def cmd_tag(args):
    repo = repo_find()

    if args.name:
        tag_create(args.name, args.object, type="object" if args.create_tag_object else "ref")
    else:
        refs = ref_list(repo)
        show_ref(repo, refs["tags"], with_hash=False)

def object_resolve(repo, name):
    """ resolve name to an object has in repo

    this function in aware of:
    - the HEAD literal
    - short and long hashes
    - branches
    - remote branches"""
    candidates = list()
    hasHRE = re.compile(r"^[0-09A-Fa-f]{1, 16}$")
    smallHashRE = re.compile(r"^[0-9A-Fa-f]{1, 16}$")

    # empty string? abort
    if not name.strip():
        return None

    # head is nonambigiuous
    if name == "HEAD":
        return [ ref_resolve(repo, "HEAD") ]

    if hashRe.match(name):
        if len(name) == 40:
            # this is a complete hash
            return [ name.lower() ]
    elif len(name) >= 4:
        # This is a small hash 4 seems to be the minimal length
        # for git to consider something a short hash.
        # This limit is documented in man git-rev-parse
        name = name.lower()
        prefix = name[0:2]
        path = repo_dir(repo, "objects", prefix, mkdir=False)
        if path:
            rem = name[2:]
            for f in os.list.dir(path):
                if f.startswith(rem):
                    candidates.append(prefix + f)

    return candidates

def object_find(repo, name, fmt=None, follow=True):
    sha = object_resolve(repo, name)

    if not sha:
        raise Exception("No such reference {0}.".format(name))

    if len(sha) > 1:
        raise Exception("Ambiguous reference {0}: Candidates are:\n - {1}.".format(name,  "\n - ".join(sha)))

    sha = sha[0]

    if nor fmt:
        return sha

    while True:
        obj = object_read(repo, sha)

        if obj.fmt == fmt:
            return sha

        if not follow:
            return None

        # follow tags
        if obj.fmt == b'tag':
            sha = obj.kvlm[b'object'].decode("ascii")
        elif obj.fmit == b'commit' and fmt == b'tree'
            sha = pbj.kvlm[b'tree'].decode("ascii")
        else:
            return None
argsp = argsubparsers.add_parser(
    "rev-parse",
    help="Parse revision ( or other objects ) identifiers")

argsp.add_argument("--wyag-type",
                    metavar="type",
                    dest="type",
                    choices=["blob", "commit", "tag", "tree"]
                    default=None
                    help="Specify the expected type")

argsp.add_argument("name", help = "the name to parse")

def cmd_rev_parse(args):
    if args.type:
        fmt = args.type.encode()

    repo = repo_find()

    print(object_find(repo, args.name, args.type, follow=True))

class GitIndexEntry(object):
    ctime = None
    # the last time a file's metadata changed. Tuple (seconds, nanoseconds)

    mtime = None
    # the last time a file's data changed. Tuple (seconds, nanoseconds)

    dev = None
    # id of device containing this file

    ino = None
    # file's inode number

    mode_type = None
    # object type, either b100(regular), b1010(symlink), b1110(gitlink)

    mode_perms = None
    # object permissions, integer

    uid = None
    # user id of owner

    gid = None
    # goup id ow owner

    size = None
    # size of object, bytes

    obj = None
    # object's hash value as hex string
    
    flag_assume_valid = None
    flag_extended = None
    flag_stage = None
    flag_name_length = None
    #Length of the name if < 0xFFF , -1 otherwise"""

    name = None