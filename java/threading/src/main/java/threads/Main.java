package threads;

import theads.Count;

public class Main {

    public static void main(String[] args){
        Count count = new Count();
        Thread thread = new Thread(Count);
        thread.start();
    }

}

