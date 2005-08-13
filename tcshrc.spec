Summary:	Tcsh dot file enhancements, complete package
Summary(pl):	Rozszerzenia konfiguracji tcsh - pe³ny pakiet
Name:		tcshrc
Version:	1.6.0
Release:	0.1
License:	GPL
Group:		Applications/Shells
Source0:	http://dl.sourceforge.net/tcshrc/%{name}-%{version}.tar.gz
# Source0-md5:	fd61940de46da9f682600eb47c44842e
Patch0:		%{name}-complete.patch
URL:		http://tcshrc.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tcshrc is a collection of dot files that enable all the available
features of the tcsh shell such as intelligent completion, aliases and
key bindings. Once install, each user can opt in and enable
individually the dot files by running 'tcshrc_config'. The
administrator can also enable tcshrc so that new users can have tcshrc
available by default. If you shell is not tcsh (for example it is
bash, run "echo $SHELL"), use 'chsh' to change to "/bin/tcsh" to use
tcsh.

%description -l pl
tcshrc to zestaw plików konfiguracyjnych w³±czaj±cych wszystkie
dostêpne mo¿liwo¶ci pow³oki tcsh, takie jak inteligentne dope³nianie,
aliasy i dowi±zania klawisze. Po zainstalowaniu ka¿dy u¿ytkownik mo¿e
w³±czaæ pojedyncze pliki konfiguracyjne uruchamiaj±c 'tcshrc_config'.
Administrator mo¿e tak¿e w³±czyæ tcshrc, aby nowi u¿ytkownicy mieli
domy¶lnie dostêpne tcshrc. Je¶li pow³ok± u¿ytkownika nie jest tcsh
(tylko np. bash - mo¿na sprawdziæ przez "echo $SHELL"), mo¿na zmieniæ
j± na "/bin/tcsh" przy u¿yciu 'chsh'.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}
cp -f tcshrc_config $RPM_BUILD_ROOT%{_bindir}
cp -f src/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING INSTALL FAQ TODO ChangeLog THANKS doc/tcshrc.pdf doc/tcshrc.ps doc/tcshrc.sgml
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
