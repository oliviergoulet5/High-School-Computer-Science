import javax.swing.*;
public class TrianglePattern {

	public static void main(String[] args) {
		String word = JOptionPane.showInputDialog(null, "Enter a word: ","Triangle Pattern",JOptionPane.QUESTION_MESSAGE);
		int length = word.length();
		for (int i=0; i<length;i++){
			System.out.println(word.substring(0, i+1));
		}
	}
}
