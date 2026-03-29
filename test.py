from lcs_algo import lcs_subsequence, lcs_length, longest_common_substring
assert lcs_subsequence("ABCBDAB", "BDCAB") in ("BCAB", "BDAB", "BCBA")
assert lcs_length("ABCBDAB", "BDCAB") == 4
assert lcs_subsequence("", "abc") == ""
assert lcs_subsequence("abc", "abc") == "abc"
assert lcs_length("abc", "def") == 0
sub = longest_common_substring("abcdef", "zbcdfg")
assert sub == "bcd"
assert longest_common_substring("abc", "xyz") == ""
assert longest_common_substring("hello", "hello") == "hello"
print("lcs_algo tests passed")
