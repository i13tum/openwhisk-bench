package analysis.functions;

public class PrimeNumber {
    public static long getNthPrimeNumber(int n) {
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
}