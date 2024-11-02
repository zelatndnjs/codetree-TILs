import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String[] ar = s.split(":");
        int a = Integer.parseInt(ar[0]);
        int b = Integer.parseInt(ar[1]);
        System.out.println((a+1) + ":"+b);
    }
}