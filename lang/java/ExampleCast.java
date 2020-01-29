class ExampleCast {
    public static void main(String[] args) {
        int price = 1250;
        double tax = 8.0;
        int total = (int) (price * (100 + tax) / 100);
        System.out.println("total:" + total);
    }
}