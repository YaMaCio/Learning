package com.IP.check;

import java.net.*;
import java.util.*;

public class InetLogic {
    public static void main(String[] args) {
        InetAddress IP = null;
        InetAddress[] ips = null;
		String url = null;
		Scanner scan = new Scanner(System.in);
        try {
            // виведення IP-адреси локального комп’ютера
            IP = InetAddress.getLocalHost();
            System.out.println("Локальний IP: " + IP);
            // виведення IP-адреси серверу ЧНУ
            IP = InetAddress.getByName("www.chdu.edu.ua");
            System.out.println("IP ЧНУ ім. Петра Могили: " + IP);
            // виведення IP-адрес серверів ЧНУ
            ips = InetAddress.getAllByName("www.chdu.edu.ua");
            System.out.println("Всі IP-адреси ЧНУ ім. Петра Могили");
            for (InetAddress ipItem: ips) {
                System.out.println(ipItem);
            }
			System.out.print("Введіть адресу сайта: ")
			url = scan.nextLine();
			IP = InetAddress.getByName(url);
            System.out.println("IP: " + IP);
            ips = InetAddress.getAllByName(url);
            System.out.println("Всі IP-адреси:");
            for (InetAddress ipItem: ips) {
                System.out.println(ipItem);
            }
        } catch (UnknownHostException ex) {
            ex.printStackTrace();
        }
    }