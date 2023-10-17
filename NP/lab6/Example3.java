package com.jnsLookUp;

import java.net.*;
import javax.swing.*;

public class JNSLookUp {
    public static void main(String[] args) {
        String hostName = null;
        if (args.length > 1)
            hostName = args[1];
        else {
            String cap = "Уведіть ім’я хосту";
            hostName = JOptionPane.showInputDialog(cap, "localhost");
            if (hostName == null)
                hostName = "localhost";
        }
        try {
            InetAddress[] ips = InetAddress.getAllByName(hostName);
            for (InetAddress IP: ips) {
                System.out.println(IP.getHostAddress());
            }
        } catch (UnknownHostException e) {
            System.out.println(e.getMessage());
        }
    }
}