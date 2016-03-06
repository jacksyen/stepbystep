var fibonacci = function (n) {
    if (typeof n !== 'number') {
        throw new Error('should be a Number');
    }

    if (n < 0) throw new Error('should be greater than Zero');
    if (n > 30) throw new Error('should be less than Thirty');
    if (n === 0) return 0;
    if (n === 1 || n === 2) return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
};

exports.fibonacci = fibonacci;

if (require.main === module) {
    var n = Number(process.argv[2]);
    console.log('fibonacci(' + n + ') is', fibonacci(n));
}

