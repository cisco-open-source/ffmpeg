Summary:        Digital VCR and streaming server
Name:           ffmpeg
Version:        2.4.3
Release:        1
%if 0%{?_with_amr:1}
License:        GPLv3+
%else
License:        GPLv2+
%endif
URL:            http://ffmpeg.org/
Source0:        ffmpeg-%{version}.tar.gz
BuildRequires:  bzip2-devel
BuildRequires:  freetype-devel
BuildRequires:  gnutls-devel
BuildRequires:  libass-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  perl(Pod::Man)
BuildRequires:  zlib-devel
BuildRequires:  yasm

%description
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.

%package        devel-static
Summary:        Development package for %{name}
Requires:       pkgconfig

%description    devel-static
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.
This package contains development files for %{name}

%global ff_configure \
./configure \\\
    --prefix=%{_prefix} \\\
    --bindir=%{_bindir} \\\
    --datadir=%{_datadir}/%{name} \\\
    --incdir=%{_includedir}/%{name} \\\
    --libdir=%{_libdir} \\\
    --mandir=%{_mandir} \\\
    --arch=%{_target_cpu} \\\
    --optflags="$RPM_OPT_FLAGS"

%prep
%setup -q -n ffmpeg-%{version}

%build
%{ff_configure}\
    --disable-devices \
    --disable-ffplay \
    --disable-ffmpeg \
    --disable-ffprobe \
    --disable-ffserver \
    --disable-doc \
    --enable-gpl \
    --enable-runtime-cpudetect \
    --enable-postproc \
    --enable-vaapi \
    --enable-vdpau \
    --enable-bzlib \
    --enable-gnutls \
    --enable-muxer=spdif \
    --enable-muxer=adts \
    --enable-muxer=asf \
    --enable-muxer=ipod \
    --enable-encoder=ac3 \
    --enable-encoder=aac \
    --enable-encoder=wmav2 \
    --enable-protocol=http \
    --enable-libvorbis \
    --enable-muxer=ogg \
    --enable-encoder=libvorbis \
    --enable-nonfree \
    --enable-pthreads \
    --enable-zlib \
%ifarch mipsel
    --disable-mips32r2 \
    --disable-mipsdspr1 \
    --disable-mipsdspr2
%endif

make %{?_smp_mflags} V=1

%install
make install DESTDIR=$RPM_BUILD_ROOT V=1

%files devel-static
%doc MAINTAINERS doc/APIchanges doc/*.txt
%{_includedir}/ffmpeg
%{_libdir}/pkgconfig/lib*.pc
%{_libdir}/lib*.a

