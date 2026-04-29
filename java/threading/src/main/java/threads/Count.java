package threads;

public class Count implements Runnable {

    @Override
    public void run() {
    
        for (int i = 0; i<=5; i++ ){
            try{
                Thread.sleep(1000);
                System.out.println(i);
            }
            catch (InterruptedException e) {
                System.out.println("Thread interrupted");
            }
        }

    }

}
