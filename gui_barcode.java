package src;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.Border;


public class gui_barcode {

	private static JFrame frame = new JFrame("Barcode Scanner");

	static String a,b,c,d, f;

	static JButton but = new JButton("Save"); 
	static JButton but2 = new JButton("Next"); 

	static JLabel manfu = new JLabel("Enter Manufacturer Name:");
	static JLabel size = new JLabel("Enter Size:");
	static JLabel text = new JLabel("Enter Serial No: ");

	static JTextField modl_no = new JTextField(12);
	static JTextField serialNo = new JTextField(12);
	static JTextField enter_size = new JTextField(3);

	static JTextField mnf = new JTextField(10);
	static JTextField enter_size2 = new JTextField(5);
	static JTextField serialNo2 = new JTextField(12);
	static JTextField modl_no2 = new JTextField(12);

	final static JLabel manfu2 = new JLabel("Manufacturer Name:");
	final static JLabel text2 = new JLabel("Serial Num: ");
	final static JLabel text3 = new JLabel("Model Num: ");
	final static JLabel size1 = new JLabel("Size:");
	static JLabel f1 = new JLabel("                  ");

	static String[] manuf = {"Western Digital", "Seagate", "Maxtor", "IBM", "Toshiba", "Conner", "Hitachi", "Other"};
	static String[] sz = {"GBs", "MBs"};

	static JComboBox drop = new JComboBox(manuf); 
	static JComboBox sz2 = new JComboBox(sz);


	static void gui() {

		JLabel t = new JLabel("                                                   ");
		JLabel t1 = new JLabel("                                                  ");
		JLabel t2 = new JLabel("                                                                           ");
		JLabel t3 = new JLabel("                                                                                                       ");
		JLabel text2 = new JLabel("Enter Model No: ");

		frame.setLayout(new FlowLayout(FlowLayout.LEFT));

		frame.add(manfu);
		frame.add(drop); 
		drop.addActionListener(new ButtonListener());
		frame.add(t);

		frame.add(text);
		frame.add(serialNo);
		frame.add(t1);

		frame.add(text2);
		frame.add(modl_no);
		frame.add(t2);

		frame.add(size); 
		frame.add(enter_size);
		frame.add(sz2);
		sz2.addActionListener(new ButtonListener());

		frame.add(t3);
		frame.add(but);
		but.addActionListener(new ButtonListener());

	}
	public static JPanel savemenu() {
		JPanel jp = new JPanel();
		jp.setLayout(new FlowLayout(FlowLayout.LEFT));
		jp.setPreferredSize(new Dimension(475,100));


		jp.add(manfu2);
		jp.add(mnf);
		jp.add(text2);
		jp.add(serialNo2);
		jp.add(text3);
		jp.add(modl_no2);
		jp.add(f1);
		jp.add(size1);
		jp.add(enter_size2);
		Border blackline = BorderFactory.createLineBorder(Color.black);
		jp.setBorder(blackline);
		return jp;

	}
	private static class ButtonListener implements ActionListener {

		public void actionPerformed(ActionEvent e) {

			a = (String) drop.getSelectedItem();

			b = (String) modl_no.getText();

			c = (String) serialNo.getText();

			d = (String) enter_size.getText();
			
			f = (String) sz2.getSelectedItem();

			if(e.getSource() == but) {
				mnf.setText(String.valueOf(a));
				modl_no2.setText(String.valueOf(b));
				serialNo2.setText(String.valueOf(c));
				enter_size2.setText(String.valueOf(d+" "+f));
			}

			if(e.getSource() == but2) {
				infowriter();
				mnf.setText("");
				modl_no.setText("");
				serialNo.setText("");
				enter_size.setText("");
				modl_no2.setText("");
				serialNo2.setText("");
				enter_size2.setText("");	
			}


		}
	}

	private static void infowriter() {
		FileWriter writer;
		try {
			
			writer = new FileWriter("C:/Users/mnasir3/eclipse-workspace/hello_java/src/src/hardrive.csv", true);
			BufferedWriter buffer = new BufferedWriter(writer);  
			buffer.write(a+", ");
			buffer.write(b+", ");
			buffer.write(c+", ");
			buffer.write(d+" "+f);
			buffer.newLine();
			buffer.close();
		} catch (IOException e) {
			e.printStackTrace();
		} 
	}

	public static void main(String[] args) {
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		gui();
		JPanel panelCheck = savemenu();
		frame.add(panelCheck);
		frame.add(but2);
		but2.addActionListener(new ButtonListener());
		frame.setSize(500,350);
		frame.setVisible(true); 

	}

}