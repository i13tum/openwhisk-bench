import com.google.gson.JsonObject;

public class PrimeNumber {
    private static long getNthPrimeNumber(int n) {
        int count = 0;
        long num = 2;
        while (count++ != n) {
            num = getNextPrimeNumber(num);
        }
        return num;
    }

    private static long getNextPrimeNumber(long n) {
        for (long i = ++n; i < n * n; i++) {
            if (isPrime(i)) return i;
        }
        return 0;
    }

    private static boolean isPrime(long n) {
        for (int i = 2; i < n; i++)
            if (n % i == 0)
                return false;
        return true;
    }

    public static void main(String[] args) {
        System.out.println(getNthPrimeNumber(5000));
    }

    public static JsonObject main(JsonObject args) {
        JsonObject response = new JsonObject();
        if (args.has("num")) {
            int num = args.getAsJsonPrimitive("num").getAsInt();
            long result = getNthPrimeNumber(num);
            response.addProperty("result", result);
        } else {
            response.addProperty("result", "No input number was provided");
        }
        return response;
    }
}