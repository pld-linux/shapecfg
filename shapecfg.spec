Summary: A configuration tool for setting traffic bandwidth parameters.
Name: shapecfg
Version: 2.0.36
Release: 4
Copyright: GPL
Group: System Environment/Base
Source: shaper.36.tar.gz
Source1: README.shaper
Patch: shapercfg-2.0.36-glibc.patch
Buildroot: /var/tmp/shaper-root
Requires: kernel >= 2.0.36
ExclusiveArch: i386

%description
The Shapecfg program configures and adjusts traffic shaper
bandwidth limiters. Traffic shaping means setting parameters
to which traffic should conform - setting the standards for
bandwidth consumption.

To use Shapecfg, you must have also installed the kernel which
supports the shaper module (kernel versions 2.0.36 or later and
late 2.1.x kernels).

Install the shapecfg package if you want to set traffic
bandwidth parameters, and if you have the appropriate
kernel.

%prep
%setup -q -n shaper
%patch0 -p1 -b .glibc

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT/sbin
install -s -m 755 shapecfg $RPM_BUILD_ROOT/sbin/shapecfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc $RPM_SOURCE_DIR/README.shaper
%defattr(-,root,root)
/sbin/shapecfg
