import assert from 'node:assert/strict';

function vowelStrings(words, queries) {
    return queries.map(([l, r]) => words.slice(l, r + 1).filter(isVowelString).length);
}

function isVowelString(word) {
    const vowels = ['a', 'e', 'i', 'o', 'u'];
    return vowels.includes(word[0]) && vowels.includes(word[word.length - 1]);
}

// example 1 - provided example
assert.deepEqual(vowelStrings(["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]]), [2, 3, 0]);

// example 2 - just vowels
assert.deepEqual(vowelStrings(["a","e","i"], [[0,2],[0,1],[2,2]]), [3, 2, 1]);

// example 3 - no words with vowels in beginning nor ending
assert.deepEqual(vowelStrings(["abaf","bcb","eceq","qaa","te"], [[0,2],[1,4],[1,1]]), [0, 0, 0]);

// example 4 - just one word (vowel)
assert.deepEqual(vowelStrings(["abfgfgfewa"], [[0, 0]]), [1]);

// example 5 - just one word (no vowel)
assert.deepEqual(vowelStrings(["abfgfgfew"], [[0, 0]]), [0]);
