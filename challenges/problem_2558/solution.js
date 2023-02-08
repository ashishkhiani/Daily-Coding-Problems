import assert from 'node:assert/strict';

function pickGifts(gifts, k) {
    for (let i = 0; i < k; i++) {
        // finds max element and its index
        let result = gifts.reduce((acc, val, index) => {
            return val > acc[0] ? [val, index] : acc;
        }, [0, 0]);

        const [maxValue, maxIndex] = result;
        gifts[maxIndex] = Math.floor(Math.sqrt(maxValue));
    }

    return gifts.reduce((acc, val) => acc + val, 0);
}

// example 1 - perfect squares
assert.equal(pickGifts([25,64,9,4,100], 4), 29);

// example 2 - just ones
assert.equal(pickGifts([1, 1, 1, 1], 4), 4);

// example 3 - not perfect squares
assert.equal(pickGifts([27, 34, 19], 3), 14)

