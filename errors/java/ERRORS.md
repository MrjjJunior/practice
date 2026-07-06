## Invalid target release

```
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-compiler-plugin:3.1:testCompile (default-testCompile) on project robot-world: Fatal error compiling: error: invalid target release: 26 -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoExecutionException
[ERROR] Failed to execute goal org.codehaus.mojo:exec-maven-plugin:3.6.3:java (default-cli) on project robot-world: An exception occurred while executing the Java class. za/co/wethinkcode/client/MainMenu has been compiled by a more recent version of the Java Runtime (class file version 65.0), this version of the Java Runtime only recognizes class file versions up to 55.0 -> [Help 1]                                           
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoExecutionException
```
This happens when you run your project maven with a different version of java jdk from sytem jdk/ with the system maven.

## Check system maven and jdk

```
java --version
mvn --version
```
Than install the matching jdk in poml.xml file 

```
sudo apt install openjdk-21-jdk

```
