// https://nackwon.tistory.com/100 보고 기능 구현하는 중
import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
	    Scanner in = new Scanner(System.in);
	    int n;
	    do {
	        System.out.println("-------------------------------------");
	        System.out.println("1.예금");
	        System.out.println("2.출금");
	        System.out.println("3.잔고");
	        System.out.println("4.종료");
	        System.out.print("원하는 기능의 번호를 입력해주세요 >> ");
	        
	        try {
	            n = in.nextInt();
	            if (n < 1 || n > 4) {
	                System.out.println("다시 입력해주세요.");
	                continue;
	            }
	            else if (n != 4) {
	                System.out.println("입력된 값은 " + n + "입니다.");
	            }
	            else {
	                System.out.println("종료를 선택했습니다.");
	                break;
	            }
	        }catch (Exception e) {
	            System.out.println("잘못된 입력입니다. 정수를 입력해주세요.");
	            continue;
	        }finally {
	            System.out.println();
	        }
	    }while(true);
	}
}