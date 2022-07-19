from typing import List


def permutations(letters: str) -> List[str]:
    """Given a list of unique letters, find all of its distinct permutations using dfs."""
    def dfs(path, used, res):
        # if we have used all letters, add the path to the result
        if len(path) == len(letters):
            res.append(path[:])
            return

        for i, letter in enumerate(letters):
            # if the letter is already used, skip it
            if used[i]:
                continue

            # mark the letter as used and add it to the path
            path.append(letter)
            used[i] = True

            # recurse
            dfs(path, used, res)

            # unmark the letter and remove it from the path
            path.pop()
            used[i] = False

    res = []
    dfs([],  # path
        [False] * len(letters),  # used
        res  # result
        )

    return res


print(permutations('abc'))
