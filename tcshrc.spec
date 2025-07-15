Summary:	Tcsh dot file enhancements, complete package
Summary(pl.UTF-8):	Rozszerzenia konfiguracji tcsh - pełny pakiet
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

%description -l pl.UTF-8
tcshrc to zestaw plików konfiguracyjnych włączających wszystkie
dostępne możliwości powłoki tcsh, takie jak inteligentne dopełnianie,
aliasy i dowiązania klawisze. Po zainstalowaniu każdy użytkownik może
włączać pojedyncze pliki konfiguracyjne uruchamiając 'tcshrc_config'.
Administrator może także włączyć tcshrc, aby nowi użytkownicy mieli
domyślnie dostępne tcshrc. Jeśli powłoką użytkownika nie jest tcsh
(tylko np. bash - można sprawdzić przez "echo $SHELL"), można zmienić
ją na "/bin/tcsh" przy użyciu 'chsh'.

%prep
%setup -q
%patch -P0 -p1

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
