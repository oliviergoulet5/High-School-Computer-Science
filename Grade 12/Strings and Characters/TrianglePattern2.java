import javax.swing.JOptionPane;

public class TrianglePattern2 {

	public static void main(String[] args) {
		String word = JOptionPane.showInputDialog(null, "Enter a word: ","Triangle Pattern",JOptionPane.QUESTION_MESSAGE);
		int length = word.length();
		int increase = 1;
		int reverseCounter = 1;
		for (int i=0; i<length*2;i++){
			if (i < length){
				System.out.println(word.substring(0, i+1));
			}else{
				System.out.println(word.substring(0, i - reverseCounter));
				reverseCounter += 2;
			}
		}
	}

}
