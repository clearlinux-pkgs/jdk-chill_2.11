PKG_NAME := jdk-chill_2.11
URL := https://repo1.maven.org/maven2/com/twitter/chill_2.11/0.8.0/chill_2.11-0.8.0.jar
ARCHIVES := https://repo1.maven.org/maven2/com/twitter/chill_2.11/0.8.0/chill_2.11-0.8.0.pom %{buildroot}

include ../common/Makefile.common
