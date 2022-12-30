public static String removeAllCharactersInTokenFromString(String token, String str) {
    String result = "";
    for (int i = 0; i < str.length(); i++) {
        if (token.indexOf(str.charAt(i)) == -1) {
            result += str.charAt(i);
        }
    }
    return result;
}