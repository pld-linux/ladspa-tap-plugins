%define		_rnam tap-plugins
Summary:	Set of LADSPA plugins for digital audio processing
Summary(pl):	Zestaw wtyczek LADSPA do cyfrowej obróbki d¼wiêku
Name:		ladspa-tap-plugins
Version:	0.5.0
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/tap-plugins/%{_rnam}-%{version}.tar.gz
# Source0-md5:	0f65959b7e368dc80bd911d06feb42cf
Patch0:		%{name}-DESTDIR_OPTFLAGS.patch
URL:		http://tap-plugins.sourceforge.net/
BuildRequires:	ladspa-devel
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of LADSPA plugins for digital audio processing, intended for use
in a professional DAW environment such as Ardour.

%description -l pl
Zestaw wtyczek LADSPA do cyfrowej obróbki d¼wiêku, których
zamierzeniem jest u¿ycie w profesjonalnym ¶rodowisku jak np. Ardour.

%prep
%setup -qn %{_rnam}-%{version}
%patch0 -p1

%build
%{__perl} -pi -e "s,\"ladspa.h\",<ladspa.h>,g" *.c
%{__make} \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/*
%attr(755,root,root) %{_libdir}/ladspa/*.so
%{_datadir}/ladspa/rdf/*.rdf
