def simplifyPath(self, path):
    """
    :type path: str
    :rtype: str
    """
    ans = []
    for s in path.split("/"):
        if s == "" or s == ".":
            continue
        elif s == "..":
            if ans:
                ans.pop()
        else:
            ans.append(s)
    return "/" + "/".join(ans)