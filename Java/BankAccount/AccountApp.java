// https://nackwon.tistory.com/100 보고 기능 구현하는 중
// 자주 발생하는 예외 : https://best421.tistory.com/10\
// 예외처리 잘 작성하는 9가지 방법 : https://hbase.tistory.com/157
import java.util.InputMismatchException;
import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    boolean run = true;  // 실행 중지를 명확하게 표현하기 위해 사용
	    int money = 0;
	    
	    // 임의 계좌 1개 생성
	    // Account account = new Account(account_num, money);
	    while (run) {
	        System.out.println("-------------------------------------");
	        System.out.println("1.예금 | 2.출금 | 3.잔고 | 4.종료");
	        System.out.println("-------------------------------------");
	        System.out.print("선택>> ");
	        
	        try {
	            int menuNo = sc.nextInt();
	            if (menuNo<1 || menuNo>4) {
	                System.out.println("범위 내에서 선택해주세요.");
	            }
	            
	            switch (menuNo) {
	                case 1:
	                    System.out.println("1번-예금을 선택");
	                    //account.deposit(money);
	                    break;
	                case 2:
	                    System.out.println("2번-출금을 선택");
	                    //account.withdraw(money);
	                    break;
	                case 3:
	                    System.out.println("3번-잔고를 선택");
	                    //account.showBalance();
	                    break;
	                case 4:
	                    System.out.println("4번-종료를 선택");
	                    run = false;
	                    break;
	                default:
	                    break;
	            }
	        }catch (InputMismatchException e) {
	            System.out.println("정수를 입력해주세요.");
	            sc.nextLine();  // 버퍼 비우기
	            continue;
	        }finally {
	            System.out.println();
	        }
	    }
		sc.close();
	}
}
