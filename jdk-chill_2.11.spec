Name     : jdk-chill_2.11
Version  : 0.8.0
Release  : 3
URL      : https://repo1.maven.org/maven2/com/twitter/chill_2.11/0.8.0/chill_2.11-0.8.0.jar
Source0  : https://repo1.maven.org/maven2/com/twitter/chill_2.11/0.8.0/chill_2.11-0.8.0.jar
Source1  : https://repo1.maven.org/maven2/com/twitter/chill_2.11/0.8.0/chill_2.11-0.8.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-chill_2.11-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-chill_2.11 package.
Group: Data

%description data
data components for the jdk-chill_2.11 package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/chill_2.11.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/chill_2.11.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/chill_2.11.xml \
%{buildroot}/usr/share/maven-poms/chill_2.11.pom \
%{buildroot}/usr/share/java/chill_2.11.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/chill_2.11.jar
/usr/share/maven-metadata/chill_2.11.xml
/usr/share/maven-poms/chill_2.11.pom
