import java.applet.Applet;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JFrame;
import javax.swing.JOptionPane;

public class KochCurve extends Applet implements ActionListener{
	TextField text;
	int intervals = 0;
	public void init(){
		text = new TextField(10);
		text.setText("Set intervals");
		text.setFocusable(true);
		text.setSelectionEnd(text.getText().length());
		text.addActionListener(this);
		this.add(text);
	};
	public void paint(Graphics g){
		super.paint(g);
		koch(g, 50, 100, getBounds().width, 100, intervals);
	};
	public void koch(Graphics g, int x1, int y1, int x5, int y5, int n){
		//n represents number of iterations we want
		int x2, y2, x3, y3, x4, y4;
		double d, a, h;

		if (n == 0 || (x5 - x1) == 0)
		{
			g.drawLine (x1, getHeight() - y1, x5, getHeight() - y5);//Draw the line
			return;
		}
		
		d = Math.sqrt ((x5-x1) * (x5-x1) + (y5-y1) * (y5-y1)) / 3;// 1/3 of the length
		a = Math.atan2 ((double) (y5-y1), (double) (x5-x1));// angle of the line
		h = 2 * d * Math.cos (30 * Math.PI / 180);// distance to peak
		
		x2 = x1 + (int) (d * Math.cos (a)); 
		y2 = y1 + (int) (d * Math.sin (a));
		x3 = x1 + (int) (h * Math.cos ((a + 30 * Math.PI / 180)));// coordinates of peak
		y3 = y1 + (int) (h * Math.sin ((a + 30 * Math.PI / 180)));
		x4 = x1 + (int) (2 * d * Math.cos (a));
		y4 = y1 + (int) (2 * d * Math.sin (a));

		koch (g, x1, y1, x2, y2, n - 1);// Recursive calls to replace line with new pattern
		koch (g, x2, y2, x3, y3, n - 1);
		koch (g, x3, y3, x4, y4, n - 1);
		koch (g, x4, y4, x5, y5, n - 1);
	};
	
	@Override
	public void actionPerformed(ActionEvent e){
		if (e.getSource() == text){
			try{
				if (Integer.parseInt(text.getText()) < 0){
					Integer.parseInt("Error");//Force catch if the text is below 0. Did this for the error message. 
				}
				intervals = Integer.parseInt(text.getText());
			}catch(Exception exception){
				text.setText("Set intervals");
				text.setFocusable(true);
				text.setSelectionEnd(text.getText().length());
				intervals = 0;
				JOptionPane.showMessageDialog(null, "ERROR: INPUT MUST BE AN INTEGER GREATER THAN 0.\nNO LETTERS OR SPECIAL CHARACTERS", "Something went wrong!", JOptionPane.ERROR_MESSAGE);
			}
			repaint();
		}
	}

}
