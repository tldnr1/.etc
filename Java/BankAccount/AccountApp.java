// https://nackwon.tistory.com/100 보고 기능 구현하는 중
import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    int num=0;
	    do {
	        System.out.println("-------------------------------------");
	        System.out.println("1.예금");
	        System.out.println("2.출금");
	        System.out.println("3.잔고");
	        System.out.println("4.종료");
	        System.out.print("원하는 기능의 번호를 입력해주세요 >> ");
	        
	        try {
	            num = sc.nextInt();
	            switch (num) {
	                case 1:
	                    System.out.println("1번-예금을 선택");
	                    break;
	                case 2:
	                    System.out.println("2번-출금을 선택");
	                    break;
	                case 3:
	                    System.out.println("3번-잔고를 선택");
	                    break;
	                case 4:
	                    System.out.println("4번-종료를 선택");
	                    break;
	                default:
	                    System.out.println("-------------------------------------");
	                    break;
	            }
	        }catch (Exception e) {
	            System.out.println("정수를 입력해주세요.");
	            sc.nextLine();  // 버퍼 비우기
	            continue;
	        }finally {
	            System.out.println();
	        }
	    }while(num!=4);
	}
}
