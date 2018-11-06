function main(params) {
    var payload = params.payload;
    if (!payload) {
        return {
            error: 'The payload is missing'
        };
    }
    return {
        result: 'Success'
    };
}