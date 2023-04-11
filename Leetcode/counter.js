var createCounter = function(n) {
    return function() {
        n += 1
        return n - 1
    };
};
