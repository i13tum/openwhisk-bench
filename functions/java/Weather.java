import com.google.gson.JsonObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class Weather {
    public static String get(String location) throws Exception {
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

    public static JsonObject main(JsonObject args) {
        JsonObject response = new JsonObject();
        if (args.has("location")) {
            String location = args.getAsJsonPrimitive("location").getAsString();
            try {
                String result = get(location);
                response.addProperty("result", result);
            } catch (Exception e) {
                response.addProperty("result", "Failed to get the response");
            }
        } else {
            response.addProperty("result", "No input was provided");
        }
        return response;
    }
}
