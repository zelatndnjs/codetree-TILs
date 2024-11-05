import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String[] arr = s.split("\\.");
        int y = Integer.parseInt(arr[0]);
        int m = Integer.parseInt(arr[1]);
        int d = Integer.parseInt(arr[2]);
        System.out.printf("%d-%d-%d",m,d,y);
    }
}