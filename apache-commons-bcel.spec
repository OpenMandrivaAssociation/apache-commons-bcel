Name:		apache-commons-bcel
Version:	6.13.0
Release:	1
Summary:	Byte Code Engineering Library
Group:		Development/Java
License:	ASL 2.0
URL:		https://commons.apache.org/proper/commons-bcel/
Source0:	https://archive.apache.org/dist/commons/bcel/source/bcel-%{version}-src.tar.gz

BuildArch:	noarch
BuildRequires:	mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:	mvn(org.apache.commons:commons-lang3)
BuildRequires:	mvn(commons-io:commons-io)
BuildRequires:	python
BuildSystem:	maven
BuildOption(install):	--file-name bcel --link %{name} --alias org.apache.bcel:bcel

%description
Apache Commons BCEL gives users a convenient way to analyze, create,
and manipulate Java class files.

%prep
%setup -q -n bcel-%{version}-src
# commons-parent already binds maven-source-plugin:jar-no-fork. This
# project's second attach-sources execution makes the plugin fail.
python - <<'PY'
from pathlib import Path
path = Path("pom.xml")
text = path.read_text()
start = text.find("<artifactId>maven-source-plugin</artifactId>")
start = text.rfind("<plugin>", 0, start)
end = text.find("</plugin>", start) + len("</plugin>")
path.write_text(text[:start] + text[end:])
PY

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
