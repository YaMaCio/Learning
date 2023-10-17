package com.urlConnections;

import java.io.*;
import java.net.*;

public class UsePostMethod {
    public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
        String message = null, strURL = null;
        try {
            message = URLEncoder.encode("my message", "UTF-8");
        } catch (UnsupportedEncodingException e1) {
            System.out.println(e1.getMessage());
        }
        try {
			System.out.print("Введіть адресу сайта: ")
			strURL = scan.nextLine();
            URL url = new URL(strURL);
            HttpURLConnection connection =
                (HttpURLConnection) url.openConnection();
            connection.setDoOutput(TRUE);
            connection.setRequestMethod("POST");
            OutputStreamWriter writer = new OutputStreamWriter(
                connection.getOutputStream());
            writer.write("message=" + message);
            writer.close();
            if (connection.getResponseCode() ==
                HttpURLConnection.HTTP_OK) {
                System.out.println(message);
            } else {
                System.out.println("Error connect");
            }
        } catch (MalformedURLException e) {
            System.out.println(e.getMessage());
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}