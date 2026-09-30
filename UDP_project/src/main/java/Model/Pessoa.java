/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Model;
/**
 *
 * @author laboratorio
 */
public class Pessoa {
    private String nome;
    private String email;
    private String token;
    private long time;

    public Pessoa() {
    }

    public Pessoa(String nome, String email, int token, int time) {
        this.nome = nome;
        this.email = email;
        this.atualizarOuManterToken();
    }

    public Pessoa(String nome, String email) {
        this.nome = nome;
        this.email = email;
    }

    public String getNome() {
        return nome;
    }
    
    public String getToken() { return token; }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setToken(String token) {
        this.token = token;
    }

    public long getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }
    
    
    public String atualizarOuManterToken() {
        long janelaAtual = System.currentTimeMillis() / 10000; // 10.000 ms = 10 segundos

        if (token == null || janelaAtual != time) {
            this.time = janelaAtual;
            int randomNum = 100000 + (int)(Math.random() * 900000);
            this.token = String.valueOf(randomNum);
        }
        return token;
    }
}
