import java.applet.Applet;
import java.awt.Color;
import java.awt.GradientPaint;
import java.awt.Graphics;

public class RecursiveTrees extends Applet{
	int maxBranches = 5;
	int colorValues[] = {100, 25, 56};
	int colorLeap[] = {30, 45, 10}; //rgb
	public void init(){}
	public void paint(Graphics g){
		//g.setColor(new Color(colorValues[0], colorValues[1], colorValues[2]));
		branch(g, (getBounds().width/2), (getBounds().height-5), 100, 90, 40, maxBranches, new Color(colorValues[0], colorValues[1], colorValues[2]));
	}
	public void branch(Graphics g, int x, int y, int length, int angle, int angleChange, int num, Color color){
		int x2,y2;//end point of x coordinate, end point of y coordinate
		if (num == 0){
			return;
		}
		x2 = (int)(x - length * Math.cos(angle*(Math.PI/180)));
		y2 = (int)(y - length * Math.sin(angle*(Math.PI/180)));
		g.drawLine(x, y, x2, y2);
		//color
		g.setColor(color);
		//recursive
		branch(g, x2, y2, length/2,angle+angleChange, angleChange, num-1,new Color(colorValues[0] + colorLeap[0], colorValues[1] + colorLeap[1]*num, colorValues[2] - colorLeap[2]));
		branch(g, x2, y2, length/2, angle-angleChange, angleChange, num-1, new Color(colorValues[0] + colorLeap[0], colorValues[1] + colorLeap[1]*num, colorValues[2] - colorLeap[2]));


	}
}
/*VARIABLES
 * x and y represents the coordinates of the start of a branch
 * length represents the length of the branch
 * angle represents the angle of the branch (in degrees)
 * angleChange represents the change of angle for the next branches
 * the level of recursion
 */
