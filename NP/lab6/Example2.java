package com.IP.check;

import java.io.IOException;
import java.net.*;

public class UnCheckedHost {
    public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String IPString = null;
        byte[] IP = {
            (byte) 217,
            (byte) 21,
            (byte) 43,
            (byte) 10
        };
        try {
            InetAddress address =
                InetAddress.getByAddress("University", IP);
            boolean accessible = address.isReachable(1000);
            String hostName = address.getHostName();
            System.out.println(hostName + " з’єднання: " + accessible);
			System.out.print("Введіть адресу сайта: ")
			IPString = scan.nextLine();
			address = InetAddress.getByName(IPString);
            accessible = address.isReachable(1000);
            String hostName = address.getHostName();
            System.out.println(hostName + " з’єднання: " + accessible);
        } catch (UnknownHostException e) {
            System.out.println("Вузол недоступний");
            e.printStackTrace();
        } catch (IOException e) {
            System.out.println("Помилка потоку");
            e.printStackTrace();
        }
    }
}