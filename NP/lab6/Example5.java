package com.url.demo;

import java.io.*;
import java.net.*;

public class printHTMLDocument {
    public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
        String dnsAddr = null;
        String fileStoreName = "C:\\temp\\index.html";
        try {
			System.out.print("Введіть адресу сайта: ")
			dnsAddr = scan.nextLine();
            URL url = new URL(dnsAddr);
            InputStreamReader isr = new
            InputStreamReader(url.openStream());
            BufferedReader buf = new BufferedReader(isr);
            FileOutputStream fos = new
            FileOutputStream(fileStoreName);
            OutputStreamWriter osw = new OutputStreamWriter(fos);
            String line = null;
            while ((line = buf.readLine()) != null) {
                System.out.println(line);
                osw.write(line);
            }
            isr.close();
            osw.close();
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}