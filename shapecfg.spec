Summary:	A configuration tool for setting traffic bandwidth parameters
Summary(pl):	Narzêdzie do konfiguracji przepustowo¶ci sieci
Name:		shapecfg
Version:	2.0.36
Release:	4
License:	GPL
Group:		Base/Utilities
Group(de):	Gründsätzlich/Werkzeuge
Group(pl):	Podstawowe/Narzêdzia
Source0:	ftp://ftp.aanet.ru/pub/Linux/system/networking/shaper.36.tar.gz
Source1:	README.shaper
Patch0:		shapercfg-2.0.36-glibc.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	kernel >= 2.0.36
ExclusiveArch:	i386

%description
The Shapecfg program configures and adjusts traffic shaper bandwidth
limiters. Traffic shaping means setting parameters to which traffic
should conform - setting the standards for bandwidth consumption.

To use Shapecfg, you must have also installed the kernel which
supports the shaper module (kernel versions 2.0.36 or later and late
2.1.x kernels).

Install the shapecfg package if you want to set traffic bandwidth
parameters, and if you have the appropriate kernel.

%description -l pl
Program shapecfg konfiguruje ograniczenia przepustowo¶ci sieci. Aby
u¿ywaæ tego pakietu trzeba mieæ j±dro z modu³em ograniczania
przepustowo¶ci - jest dostêpny od wersji 2.0.36 lub pó¼nych 2.1.x.

%prep
%setup -q -n shaper
%patch0 -p1

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/sbin
install -m 755 shapecfg $RPM_BUILD_ROOT/sbin/shapecfg

cp -f %{SOURCE1} .
gzip -9nf README.shaper

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.shaper.gz
%attr(755,root,root) /sbin/shapecfg
