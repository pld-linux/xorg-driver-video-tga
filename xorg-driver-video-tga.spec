Summary:	X.org video driver for TGA (DEC 21030) video chips
Summary(pl):	Sterownik obrazu X.org dla uk³adów graficznych TGA (DEC 21030)
Name:		xorg-driver-video-tga
Version:	1.0.0.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-video-tga-%{version}.tar.bz2
# Source0-md5:	375d1061101f7088edda8bdabc110afa
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for TGA (DEC 21030) video chips.

%description -l pl
Sterownik obrazu X.org dla uk³adów graficznych TGA (DEC 21030).

%prep
%setup -q -n xf86-video-tga-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/tga_drv.so
#%{_mandir}/man4/tga.4x*
