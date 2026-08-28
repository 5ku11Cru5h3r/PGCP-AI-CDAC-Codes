# n=input("Enter a string:")
# vowels=['a','e','i','o','u']
# if vowels in n:


def vowel_frequency_2():
    vect = []
    for i in range(26):
        vect.append(0)
    vowel_count = 0
    user_input = input("Enter string :")
    for i in user_input:
        if i in "aeiou":
            vect[ord(i) - ord("a")] += 1
            vowel_count += 1
    print(f"a = {vect[ord('a')-ord('a')]}")
    print(f"e = {vect[ord('e')-ord('a')]}")
    print(f"i = {vect[ord('i')-ord('a')]}")
    print(f"o = {vect[ord('o')-ord('a')]}")
    print(f"u = {vect[ord('u')-ord('a')]}")
    print(f"Consonants are:  {len(user_input)-vowel_count}")


def vowel_frequency():
    """
        Write a program that prompts the user to enter a string and counts:

    1. The individual frequency of each vowel (`a`, `e`, `i`, `o`, `u`), case-insensitively.
    2. The total count of all consonants.

    - **Sample Input**: `"Vinod Kumar Kayartaya"`
    - **Sample Output**:
      ```text
      Vowel Frequencies:
      a: 4
      e: 0
      i: 1
      o: 1
      u: 1
      Total Consonants: 12
      ```
    """
    user_input = input("Enter string :")

    data_dictionary = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    v = 0
    for i in user_input:
        if i in "aeiou":

            data_dictionary[i] += 1
            v += 1

    print(f"a = {data_dictionary['a']}")
    print(f"e = {data_dictionary['e']}")
    print(f"i = {data_dictionary['i']}")
    print(f"o = {data_dictionary['o']}")
    print(f"u = {data_dictionary['u']}")
    print(f"Consonants are:  {len(user_input)-v}")
    ...


def main():
    vowel_frequency_2()


...


if __name__ == 'main':
    main()