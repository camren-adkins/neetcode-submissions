class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        String encoded = null;
        if (!strs.isEmpty()) {
            //replace empty stringsf and add delimiters
            for (int i = 0; i < strs.size()-1; i++) {
                if (strs.get(i) == "") sb.append("ABC?");
                sb.append(strs.get(i)).append("A#");
            }
            //adds and replaces last if empty otherwise adds last
            if (strs.getLast() == "") sb.append("ABC?");
            sb.append(strs.getLast());
        encoded = sb.toString();
        }
        return encoded;
    }

    public List<String> decode(String str) {
        List<String> decoded = new ArrayList<>();
        if (str != null) {
             System.out.println("String: " + str);
            String[] stringList = str.split("A#");
            System.out.println(stringList.length);
            for (int i = 0; i < stringList.length; i ++) {
                stringList[i] = stringList[i].replace("ABC?", "");
            }
            System.out.println(Arrays.toString(stringList));
            for (String s : stringList) {
                decoded.add(s);
            }
        }
        return decoded;
    }
}
