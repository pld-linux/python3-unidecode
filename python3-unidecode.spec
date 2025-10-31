#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	Unidecode
Summary:	ASCII transliterations of Unicode text
Summary(pl.UTF-8):	Transliteracje ASCII tekstu w Unicode
Name:		python3-unidecode
Version:	1.4.0
Release:	1
License:	GPL v2+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/unidecode/
Source0:	https://files.pythonhosted.org/packages/source/U/Unidecode/%{module}-%{version}.tar.gz
# Source0-md5:	d3da666a6d0e2729039556e5f0026480
URL:		https://pypi.org/project/Unidecode/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unidecode provides a function, 'unidecode(...)' that takes Unicode
data and tries to represent it in ASCII characters (i.e., the
universally displayable characters between 0x00 and 0x7F). The
representation is almost always an attempt at transliteration - i.e.,
conveying, in Roman letters, the pronunciation expressed by the text
in some other writing system.

This is a Python port of Text::Unidecode Perl module by Sean M. Burke.

%description -l pl.UTF-8
Unidecode udostępnia funkcję "unidecode(...)", pobierającą dane
kodowane Unicode i próbuje reprezentawać je przy użyciu znaków ASCII
(tj. znaków uniwersalnie możliwych do wyświetlenia, o kodach od 0x00
do 0x7F). Reprezentacja jest prawie zawsze próbą transliteracji - tzn.
przekazaniem, przy użyciu liter rzymskich, wymowy wyrażanej przez
tekst w jakimś innym systemie pisma.

Moduł jest pythonowym portem modułu Perla Text::Unidecode autorstwa
Seana M. Burke.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
LC_ALL=C.UTF-8 \
%{__python3} -m unittest discover -s tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/unidecode{,-3}
ln -s unidecode-3 $RPM_BUILD_ROOT%{_bindir}/unidecode
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.rst
%attr(755,root,root) %{_bindir}/unidecode-3
%{_bindir}/unidecode
%{py3_sitescriptdir}/unidecode
%{py3_sitescriptdir}/Unidecode-%{version}-py*.egg-info
