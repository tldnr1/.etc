public class Account {
    // 외부에서 변경되면 안되기 때문에 private으로 작성
    private String accountNo;  // 계좌번호
    private int balance = 0;  // 잔고

    public Account(String accountNo) {
        this.accountNo = accountNo;
    }

    public void deposit(int money) {
        balance = balance + money;
        System.out.println("예금액 : " + money);
    }

    public void withdraw(int money) {
        balance = balance - money;
        System.out.println("출금액 : " + money);
    }

    public void showBalance() {
        System.out.println("잔고 : " + balance);
    }
}
