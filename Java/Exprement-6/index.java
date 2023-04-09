// import java.io.File;

// public class index {
//   public static void main(String[] args) {
    
//     File file = new File("first.txt");

//     try {
//       if (file.createNewFile()) {
//         System.out.println("File created: " + file.getName());
//       } else {
//         System.out.println("File already exists.");
//       }
//     } catch (Exception e) {
//       System.out.println("An error occurred.");
//       e.printStackTrace();
//     }

//     System.out.println("Absolute path: " + file.getAbsolutePath());
//     System.out.println("Readable: " + file.canRead());
//     System.out.println("Writable: " + file.canWrite());
//     System.out.println("Executable: " + file.canExecute());
//     System.out.println("Length (in bytes): " + file.length());
//     System.out.println("Is a file: " + file.isFile());
//     System.out.println("Is a directory: " + file.isDirectory());
//     System.out.println("Exists: " + file.exists());
    
//   }
// }


// import java.io.File;

// public class index {
//   public static void main(String[] args) {
    
//     // Create a new file called "second.txt"
//     File file = new File("second.txt");

//     try {
//       if (file.createNewFile()) {
//         System.out.println("File created: " + file.getName());
//       } else {
//         System.out.println("File already exists.");
//       }
//     } catch (Exception e) {
//       System.out.println("An error occurred.");
//       e.printStackTrace();
//     }

//     // Rename the file to "renamed.txt"
//     File renamedFile = new File("renamed.txt");
//     if (file.renameTo(renamedFile)) {
//       System.out.println("File renamed successfully.");
//     } else {
//       System.out.println("Failed to rename file.");
//     }
//   }
// }

// import java.io.File;

// public class index {
//   public static void main(String[] args) {
    
//     // Create a new file called "second.txt"
//     File file = new File("second.txt");

//     try {
//       if (file.createNewFile()) {
//         System.out.println("File created: " + file.getName());
//       } else {
//         System.out.println("File already exists.");
//       }
//     } catch (Exception e) {
//       System.out.println("An error occurred.");
//       e.printStackTrace();
//     }

//     // Rename the file to "renamed.txt"
//     File renamedFile = new File("renamed.txt");
//     if (file.renameTo(renamedFile)) {
//       System.out.println("File renamed successfully.");
//     } else {
//       System.out.println("Failed to rename file.");
//     }

//     // Delete the file
//     if (renamedFile.delete()) {
//       System.out.println("File deleted successfully.");
//     } else {
//       System.out.println("Failed to delete file.");
//     }
//   }
// }

import java.io.File;

class File
{
public static void main(String args[])
{
try
{
File f=new File("D\File\");

}
catch()

{
System.out.println(i);
}
}
}