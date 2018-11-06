import com.google.gson.JsonObject;
import java.util.ArrayList;
import java.util.List;

public class Matrix {
    private static long[][] multiplyMatrices(long[][] m1, long[][] m2, int size) {
        long[][] result = new long[size][size];
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                int sum = 0;
                for (int k = 0; k < size; k++) {
                    sum += m1[i][k] * m2[k][j];
                }
                result[i][j] = sum;
            }
        }
        return result;
    }

    private static long[][] generateMatrix(int size) {
        long[][] matrix = new long[size][size];
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                long number = Math.round(117 + Math.random() * 40);
                matrix[i][j] = number;
            }
        }
        return matrix;
    }

    public static JsonObject main(JsonObject args) {
        JsonObject response = new JsonObject();
        if (args.has("size") && args.has("ramLoader")) {
            int size = args.getAsJsonPrimitive("size").getAsInt();
            long ramLoader = args.getAsJsonPrimitive("size").getAsLong();

            long[][] m1 = generateMatrix(size);
            long[][] m2 = generateMatrix(size);

            List<Object> fakeList = new ArrayList<>();

            for (int k = 0; k < ramLoader; k++) {
                fakeList.add(m1[k % 9].clone());
            }

            multiplyMatrices(m1, m2, size);
            response.addProperty("result", "Success");
        } else {
            response.addProperty("result", "No input number was provided");
        }
        return response;
    }
}
