package analysis.functions;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class Weather {
    private static String get(String location) throws Exception {
        StringBuilder result = new StringBuilder();
        String urlString = "https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text='<<Location>>')&format=json";
        URL url = new URL(urlString.replace("<<Location>>", location));
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");
        BufferedReader rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String line;
        while ((line = rd.readLine()) != null) {
            result.append(line);
        }
        rd.close();
        return result.toString();
    }

    public static String getWeather(String location) {
        try {
            return get(location);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }
}
