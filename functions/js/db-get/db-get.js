function myAction(params) {

  return new Promise(function(resolve, reject) {
    console.log('Connecting to MySQL database');
    var mysql = require('promise-mysql');
    var connection;
    mysql.createConnection({
      host: params.MYSQL_HOSTNAME,
      user: params.MYSQL_USERNAME,
      password: params.MYSQL_PASSWORD,
      database: params.MYSQL_DATABASE
    }).then(function(conn) {
      connection = conn;
      console.log('Querying');
      var queryText = 'SELECT SLEEP(?) as result';
      var result = connection.query(queryText, [params.delay]);
      connection.end();
      return result;
    }).then(function(result) {
      console.log('Extracted result');
      if (result) {
        console.log('final result: ' + result[0].result);
        resolve({
          result: 'Success'
        });
      } else {
        console.log('Failed to extract result');
        reject({
          headers: {
            'Content-Type': 'application/json'
          },
          statusCode: 404,
          body: {
            error: "Not found."
          }
        });
      }
    }).catch(function(error) {
      if (connection && connection.end) connection.end();
      console.log(error);
      reject({
        headers: {
          'Content-Type': 'application/json'
        },
        statusCode: 500,
        body: {
          error: "Error."
        }
      });
    });
  });

}

/*myAction({
  MYSQL_HOSTNAME: '172.24.63.183',
  MYSQL_USERNAME: 'root',
  MYSQL_PASSWORD: 'aa',
  MYSQL_DATABASE: 'test',
  id: 1
});*/

exports.main = myAction;