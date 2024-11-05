import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sc.useDelimiter(":");
        int a = sc.nextInt();
        int b = sc.nextInt();
        a += 1;
        System.out.println(a+":"+b);
        
    }
}