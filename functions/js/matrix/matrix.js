function multiplyMatrices(m1, m2) {
    var result = [];
    for (var i = 0; i < m1.length; i++) {
        result[i] = [];
        for (var j = 0; j < m2[0].length; j++) {
            var sum = 0;
            for (var k = 0; k < m1[0].length; k++) {
                sum += m1[i][k] * m2[k][j];
            }
            result[i][j] = sum;
        }
    }
    return result;
}

function generateMatrix(size) {
    var matrix = [];
    for (var i = 0; i < size; i++) {
        var row = [];
        for (var j = 0; j < size; j++) {
            row.push(Math.round(117 + Math.random() * 40));
        }
        matrix.push(row);
    }
    return matrix;
}

function main(params) {
    if (!params.size) {
        return {
            result: "Matrix size is required"
        }
    }
    if (!params.ramLoader) {
        return {
            result: "ramLoader is required"
        }
    }

    var fakeList = [];

    var m1 = generateMatrix(params.size);
    var m2 = generateMatrix(params.size);

    for (var k = 0; k < params.ramLoader; k++) {
        fakeList.push(m1[k % 9].slice(0))
    }

    var result = multiplyMatrices(m1, m2);

    return {
    	result: 'Success'
    };
}