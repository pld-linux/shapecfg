Summary:	A configuration tool for setting traffic bandwidth parameters.
Name:		shapecfg
Version:	2.0.36
Release:	4
License:	GPL
Group:		Base/Utilities
Group(pl):	Podstawowe/Narzêdzia
Source0:	shaper.36.tar.gz
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

%prep
%setup -q -n shaper
%patch0 -p1 -b .glibc

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/sbin
install -s -m 755 shapecfg $RPM_BUILD_ROOT/sbin/shapecfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc $RPM_SOURCE_DIR/README.shaper
%defattr(-,root,root)
/sbin/shapecfg
